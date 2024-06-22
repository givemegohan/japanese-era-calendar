#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import csv
import bisect

file_path = 'jp_era_cal_min.csv'

def getDateInt(year, month, day):
    return year * 10000 + month * 100 + day

def read_csv(file_path):
    data = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['Common year'] = int(row['Common year'])
            row['Common month'] = int(row['Common month'])
            row['Common day'] = int(row['Common day'])
            data.append(row)
    return data

def find_japanese_date(data, target_date):
    common_dates = [getDateInt(row['Common year'],row['Common month'],row['Common day']) for row in data]
    
    index = bisect.bisect_left(common_dates, target_date)
    
    if index < len(data) and common_dates[index] == target_date:
        return data[index]
    elif index > 0:
        previous_row = data[index - 1]
        prev_date = common_dates[index - 1]
        diff_days = target_date - prev_date

        new_row = {
            'Common year': int(previous_row['Common year']),
            'Common month': int(previous_row['Common month']),
            'Common day': int(previous_row['Common day']) + diff_days,
            'Era name': previous_row['Era name'],
            'Japanese year': int(previous_row['Japanese year']),
            'Japanese month': int(previous_row['Japanese month']),
            'Japanese day': int(previous_row['Japanese day']) + diff_days,
            'Is leap month': previous_row['Is leap month']
        }
        return new_row

    return None

def main():
    data = read_csv(file_path)
    target_date = getDateInt(1234, 5, 6)
    result = find_japanese_date(data, target_date)
    
    if result:
        japanese_month_display = f"閏{result['Japanese month']}" if result['Is leap month'] == '1' else f"{result['Japanese month']}"
        print(f"Common Date: {result['Common year']}-{result['Common month']:02d}-{result['Common day']:02d}")
        print(f"Japanese Date: {result['Era name']}{result['Japanese year']}年{japanese_month_display}月{result['Japanese day']}日")
    else:
        print("Date not found")

if __name__ == "__main__":
    main()