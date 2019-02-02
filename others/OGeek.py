# -*- coding: utf-8 -*-
'''
@author: xiongyongfu
@contact: xyf_0704@sina.com
@file: OGeek.py
@Software: PyCharm
@time: 2018/10/13 17:45
@desc:
'''

import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import f1_score

train_data = pd.read_table('C:\\Users\\Administrator\\Downloads\\OGeek\\oppo_round1_train_20180929\\oppo_round1_train_20180929.txt',
        names= ['prefix','query_prediction','title','tag','label'], header= None, encoding='utf-8').astype(str)
val_data = pd.read_table('C:\\Users\\Administrator\\Downloads\\OGeek\\oppo_round1_vali_20180929\\oppo_round1_vali_20180929.txt',
        names = ['prefix','query_prediction','title','tag','label'], header = None, encoding='utf-8').astype(str)
test_data = pd.read_table('C:\\Users\\Administrator\\Downloads\\OGeek\\oppo_round1_test_A_20180929\\oppo_round1_test_A_20180929.txt',
        names = ['prefix','query_prediction','title','tag'],header = None, encoding='utf-8').astype(str)
train_data = train_data[train_data['label'] != '音乐' ]
test_data['label'] = -1

train_data = pd.concat([train_data,val_data])
train_data['label'] = train_data['label'].apply(lambda x: int(x))
test_data['label'] = test_data['label'].apply(lambda x: int(x))
items = ['prefix', 'title', 'tag']


temp0=train_data.groupby(items, as_index=False)['label'].agg({'_'.join(items)+'_click': 'sum','_'.join(items)+'count':'count'})
temp0['_'.join(items)+'_ctr'] = temp0['_'.join(items)+'_click']/(temp0['_'.join(items)+'count']+3)
train_data = pd.merge(train_data, temp0, on=items, how='left')
test_data = pd.merge(test_data, temp0, on=items, how='left')

for item in items:
    temp = train_data.groupby(item, as_index = False)['label'].agg({item+'_click':'sum', item+'_count':'count'})
    temp[item+'_ctr'] = temp[item+'_click']/(temp[item+'_count'])
    train_data = pd.merge(train_data, temp, on=item, how='left')
    test_data = pd.merge(test_data, temp, on=item, how='left')
for i in range(len(items)):
    for j in range(i+1, len(items)):
        item_g = [items[i], items[j]]
        temp = train_data.groupby(item_g, as_index=False)['label'].agg({'_'.join(item_g)+'_click': 'sum','_'.join(item_g)+'count':'count'})
        temp['_'.join(item_g)+'_ctr'] = temp['_'.join(item_g)+'_click']/(temp['_'.join(item_g)+'count']+3)
        train_data = pd.merge(train_data, temp, on=item_g, how='left')
        test_data = pd.merge(test_data, temp, on=item_g, how='left')


#prefix 与title 相等的情况
items1=['prefix','title']
temp1= train_data[(train_data['prefix']==train_data['title'])]
temp2= temp1.groupby(items1, as_index=False)['label'].agg({'_'.join(items1)+'_eq_click': 'sum','_'.join(items1)+'_eq_click':'count'})
temp2['_'.join(items1)+'_eq_ctr'] = temp2['_'.join(items1)+'_eq_click']/(temp2['_'.join(items1)+'_eq_click'])
train_data = pd.merge(train_data, temp2, on=items1, how='left')
test_data = pd.merge(test_data, temp2, on=items1, how='left')


def function1(a, b):
    if a == b:
        return 1
    else:
        return 0
cond1=train_data['prefix']==train_data['title']
cond2=test_data['prefix']==test_data['title']
train_data['pretile_is_eq'] = np.where(cond1,1,0)
test_data['pretile_is_eq'] = np.where(cond2,1,0)
#train_data['pretile_is_eq'] = train_data.apply(lambda x: function1(train_data.prefix,train_data.title), axis = 1)
#test_data['pretile_is_eq'] = test_data.apply(lambda x: function1(test_data['prefix'], test_data['title']), axis = 1)



train_data['ctr2_3sum'] = train_data['prefix_title_ctr']*0.2+train_data['prefix_tag_ctr']*0.2+train_data['title_tag_ctr']*0.2+train_data['prefix_title_tag_ctr']*0.4
test_data['ctr2_3sum']= test_data['prefix_title_ctr']*0.2+test_data['prefix_tag_ctr']*0.2+test_data['title_tag_ctr']*0.2+test_data['prefix_title_tag_ctr']*0.4


train_data_ = train_data.drop(['prefix', 'query_prediction', 'title', 'tag'], axis = 1)
test_data_ = test_data.drop(['prefix', 'query_prediction', 'title', 'tag'], axis = 1)

print('train beginning')

X = np.array(train_data_.drop(['label'], axis = 1))
y = np.array(train_data_['label'])
X_test_ = np.array(test_data_.drop(['label'], axis = 1))
print('================================')
print(X.shape)
print(y.shape)
print('================================')


xx_logloss = []
xx_submit = []
N = 5
skf = StratifiedKFold(n_splits=N, random_state=42, shuffle=True)

params = {
    'boosting_type': 'gbdt',
    'objective': 'binary',
    'metric': 'binary_logloss',
    'num_leaves': 32,
    'learning_rate': 0.05,
    'feature_fraction': 0.8,
    'bagging_fraction': 0.8,
    'bagging_freq': 5,
    'verbose': 1
}

for k, (train_in, test_in) in enumerate(skf.split(X, y)):
    print('train _K_ flod', k)
    X_train, X_test, y_train, y_test = X[train_in], X[test_in], y[train_in], y[test_in]

    lgb_train = lgb.Dataset(X_train, y_train)
    lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train)

    gbm = lgb.train(params,
                    lgb_train,
                    num_boost_round=5000,
                    valid_sets=lgb_eval,
                    early_stopping_rounds=50,
                    verbose_eval=50,
                    )
    print(f1_score(y_test, np.where(gbm.predict(X_test, num_iteration=gbm.best_iteration)>0.5, 1,0)))
    xx_logloss.append(gbm.best_score['valid_0']['binary_logloss'])
    xx_submit.append(gbm.predict(X_test_, num_iteration=gbm.best_iteration))

print('train_logloss:', np.mean(xx_logloss))
s = 0
for i in xx_submit:
    s = s + i

test_data_['label'] = list(s / N)
test_data_['label'] = test_data_['label'].apply(lambda x: round(x))
print('test_logloss:', np.mean(test_data_.label))
test_data_['label'].to_csv('C:\\Users\\Administrator\\Downloads\\OGeek\\result.csv',index = False)