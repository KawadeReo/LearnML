import pandas as pd
import kaggle 




#-------------------------------------------------------

product_data = pd.DataFrame({   #表形式のデータを作成する DataFrame
    'Bob': ['I liked it.','It was auful.'],
    'Sue': ['Pretty good.', 'Bland.']
},
index = ['product A', 'product B'])

# print(product_data)
#                      Bob           Sue
# product A    I liked it.  Pretty good.
# product B  It was auful.        Bland.about:blank#blocked


#-------------------------------------------------------

series_data = pd.Series([   #１次元のデータを作成する
    1,2,3,4,5
])

# print(series_data)
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64

#-------------------------------------------------------
#kaggleのライブラリでデータセットをダウンロード。 kaggle datasets download -d zynicide/wine-reviews


#csvに最初からインデックスが含まれている場合、主キーのカラムを指示できる　index_col
wine_reviews = pd.read_csv(r"E:\python\udemy\wine-reviews\winemag-data-130k-v2.csv",index_col=0) #ローカルのパス。udemyは関係ない csvからデータ作成

# print(wine_reviews.shape)   #データのカラムとレコード数
# print(wine_reviews.head)  #データの最初の数行を確認     
# (129971, 13)
#     country                                        description                         designation  ...                                              title         variety               winery
# 0     Italy  Aromas include tropical fruit, broom, brimston...                        Vulkà Bianco  ...                  Nicosia 2013 Vulkà Bianco  (Etna)     White Blend              Nicosia
# 1  Portugal  This is ripe and fruity, a wine that is smooth...                            Avidagos  ...      Quinta dos Avidagos 2011 Avidagos Red (Douro)  Portuguese Red  Quinta dos Avidagos
# 2        US  Tart and snappy, the flavors of lime flesh and...                                 NaN  ...      Rainstorm 2013 Pinot Gris (Willamette Valley)      Pinot Gris            Rainstorm
# 3        US  Pineapple rind, lemon pith and orange blossom ...                Reserve Late Harvest  ...  St. Julian 2013 Reserve Late Harvest Riesling ...        Riesling           St. Julian
# 4        US  Much like the regular bottling from 2012, this...  Vintner's Reserve Wild Child Block  ...  Sweet Cheeks 2012 Vintner's Reserve Wild Child...      Pinot Noir         Sweet Cheeks

#特定カラムが見たい場合、.designation等カラム名を入れれば見れる  reviews['country']も可
# wine_reviews.country
# wine_reviews['country']   #基本的にこっちの方が良さそう
# wine_reviews['country'][0]
# wine_reviews.iloc[0]  #特定のカラム
# wine_reviews.iloc[:,0]  #特定のレコードとカラムを指定　(行,列)excelVBAと同じ ':'は全てを選択
# wine_reviews.iloc[1:3,0]
# wine_reviews.iloc[[1,3,4],0]
# wine_reviews.iloc[-5]   
# wine_reviews.loc[0,'country'] #loc

# loc と iloc の使い分け
# loc と iloc を使い分ける際、1つ注意すべき「落とし穴」があります。両者は範囲指定の方法が微妙に異なります。

# iloc は Python 標準ライブラリのスライスと同じで、開始位置を含み、終了位置は含みません。つまり 0:10 はインデックス 0 ～ 9 を選択します (合計10要素)。
# loc は開始位置と終了位置の両方を含みます。つまり 0:10 はインデックス 0 ～ 10 を選択します (合計11要素)。



#wine_reviews.set_index('title')    #インデックスの変更

#-------------------------------------------------------

# print(wine_reviews.country == 'Italy')
# print(wine_reviews.loc[wine_reviews.country == 'Italy'])    #条件を満たすレコードの選択
# print(wine_reviews.loc[(wine_reviews.country == 'Italy') & (wine_reviews.points >= 90)]) #複数条件を満たすレコードの選択
#        country                                        description                designation  ...                                              title       variety                           winery
# 120      Italy  Slightly backward, particularly given the vint...        Bricco Rocche Prapó  ...         Ceretto 2003 Bricco Rocche Prapó  (Barolo)      Nebbiolo                          Ceretto
# 130      Italy  At the first it was quite muted and subdued, b...      Bricco Rocche Brunate  ...       Ceretto 2003 Bricco Rocche Brunate  (Barolo)      Nebbiolo                          Ceretto
# 133      Italy  Einaudi's wines have been improving lately, an...                        NaN  ...                  Poderi Luigi Einaudi 2003  Barolo      Nebbiolo             Poderi Luigi Einaudi
# 135      Italy  The color is just beginning to show signs of b...                     Sorano  ...              Giacomo Ascheri 2001 Sorano  (Barolo)      Nebbiolo                  Giacomo Ascheri
# 140      Italy  A big, fat, luscious wine with plenty of toast...                Costa Bruna  ...    Poderi Colla 2005 Costa Bruna  (Barbera d'Alba)       Barbera                     Poderi Colla
# ...        ...                                                ...                        ...  ...                                                ...           ...                              ...
# 129929   Italy  This luminous sparkler has a sweet, fruit-forw...                        NaN  ...  Col Vetoraz Spumanti NV  Prosecco Superiore di...      Prosecco             Col Vetoraz Spumanti
# 129943   Italy  A blend of Nero d'Avola and Syrah, this convey...                    Adènzia  ...  Baglio del Cristo di Campobello 2012 Adènzia R...     Red Blend  Baglio del Cristo di Campobello
# 129947   Italy  A blend of 65% Cabernet Sauvignon, 30% Merlot ...                   Symposio  ...  Feudo Principi di Butera 2012 Symposio Red (Te...     Red Blend         Feudo Principi di Butera
# 129961   Italy  Intense aromas of wild cherry, baking spice, t...                        NaN  ...                        COS 2013 Frappato (Sicilia)      Frappato                              COS
# 129962   Italy  Blackberry, cassis, grilled herb and toasted a...  Sàgana Tenuta San Giacomo  ...  Cusumano 2012 Sàgana Tenuta San Giacomo Nero d...  Nero d'Avola                         Cusumano

# print(wine_reviews.loc[wine_reviews.country.isin(['Itary','France'])])  #locで行を取得できる　isinノミなどの場合はtrue/falseで出てくる
#wine_reviews.country.isin 値があるか
#wine_reviews.country.notnull() NaNじゃないか(この場合国のカラムが無い場合)

#-------------------------------------------------------

wine_reviews['critic'] = 'everyone'
wine_reviews['critic'] = range(len(wine_reviews),0,-1)  #Datasetにデータを追加する
print(wine_reviews)
#          country                                        description                             designation  ...         variety                                    winery    critic
# 0          Italy  Aromas include tropical fruit, broom, brimston...                            Vulkà Bianco  ...     White Blend                                   Nicosia  everyone
# 1       Portugal  This is ripe and fruity, a wine that is smooth...                                Avidagos  ...  Portuguese Red                       Quinta dos Avidagos  everyone
# 2             US  Tart and snappy, the flavors of lime flesh and...                                     NaN  ...      Pinot Gris                                 Rainstorm  everyone
# 3             US  Pineapple rind, lemon pith and orange blossom ...                    Reserve Late Harvest  ...        Riesling                                St. Julian  everyone
# 4             US  Much like the regular bottling from 2012, this...      Vintner's Reserve Wild Child Block  ...      Pinot Noir                              Sweet Cheeks  everyone
# ...          ...                                                ...                                     ...  ...             ...                                       ...       ...
# 129966   Germany  Notes of honeysuckle and cantaloupe sweeten th...  Brauneberger Juffer-Sonnenuhr Spätlese  ...        Riesling  Dr. H. Thanisch (Erben Müller-Burggraef)  everyone
# 129967        US  Citation is given as much as a decade of bottl...                                     NaN  ...      Pinot Noir                                  Citation  everyone
# 129968    France  Well-drained gravel soil gives this wine its c...                                   Kritt  ...  Gewürztraminer                           Domaine Gresser  everyone
# 129969    France  A dry style of Pinot Gris, this is crisp with ...                                     NaN  ...      Pinot Gris                      Domaine Marcel Deiss  everyone
# 129970    France  Big, rich and off-dry, this is powered by inte...           Lieu-dit Harth Cuvée Caroline  ...  Gewürztraminer                          Domaine Schoffit  everyone