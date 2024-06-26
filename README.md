# japanese-era-calendar
元号カレンダー

# 説明
日本の元号を検索性の良い形式で提供します。

# 内容
## 概要
以下のような表のCSVファイルです。(jp_era_cal_min.csvから抜粋)

|Modified Julian Date|UNIX time|Julian/Gregorian|Common year|Common month|Common day|Imperial era|Era name|Japanese year|Northern Court era name|Northern Court year|Is leap month|Japanese month|Japanese day|
|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|
|-93977|-11626329600|G|1601|7|30|2261|慶長|6| | |0|7|1|
|-93975|-11626156800|G|1601|8|1|2261|慶長|6| | |0|7|3|
|-93948|-11623824000|G|1601|8|28|2261|慶長|6| | |0|8|1|
|-93944|-11623478400|G|1601|9|1|2261|慶長|6| | |0|8|5|
|-93919|-11621318400|G|1601|9|26|2261|慶長|6| | |0|9|1|
|-93914|-11620886400|G|1601|10|1|2261|慶長|6| | |0|9|6|
|-93889|-11618726400|G|1601|10|26|2261|慶長|6| | |0|10|1|
|-93883|-11618208000|G|1601|11|1|2261|慶長|6| | |0|10|7|
|-93859|-11616134400|G|1601|11|25|2261|慶長|6| | |0|11|1|

## 列の説明
|列名|説明|
|:----|:----|
|Modified Julian Date| 修正ユリウス日。1858年11月17日を0とした通算日。|
|UNIX time| UNIX time。1970年1月1日午前0時0分0秒を0とした通算秒。|
|Julian/Gregorian| 西暦がユリウス暦の場合は"J"、グレゴリオ暦の場合は"G"。1582年10月4日まではユリウス暦、その翌日がグレゴリオ暦の1582年10月15日。|
|Common year| 西暦の年。紀元前はマイナス表記。|
|Common month| 西暦の月。|
|Common day| 西暦の日。|
|Imperial era| 皇紀、神武天皇即位紀元。西暦の紀元前660年（-659年）を1年とした紀年法。|
|Era name|元号。南北朝時代の場合は南朝。|
|Japanese year|和暦の年。南北朝時代の場合は南朝。|
|Northern Court era name|北朝の年号。該当しない場合は空。|
|Northern Court year|北朝の年。該当しない場合は空。|
|Is leap month|閏月フラグ。閏月の場合は1、そうでない場合は0。|
|Japanese month|和暦の月。|
|Japanese day|和暦の日。|

## 提供ファイル
|ファイル名|説明|
|:----|:----|
|jp_era_cal_full.csv.gz| 皇紀1年1月1日つまり西暦-659年2月18日から西暦2100年12月31日までの全日データ。gzip圧縮。|
|jp_era_cal_min.csv| 上記のうち、改元が行われた日、和暦・西暦での各月1日、日が飛んだ日のみのデータを抽出したもの。|

# 参照したデータ
国立天文台の暦計算室（[https://eco.mtk.nao.ac.jp/koyomi/](https://eco.mtk.nao.ac.jp/koyomi/)）の提供データに基づきます。
