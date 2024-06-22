#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import csv
import bisect

file_path = 'jp_era_cal_min.csv'

def read_csv(file_path):
    data = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['Modified Julian Date'] = int(row['Modified Julian Date'])
            data.append(row)
    return data

def find_date(data, target_mjd):
    mjd_list = [row['Modified Julian Date'] for row in data]
    
    index = bisect.bisect_left(mjd_list, target_mjd)
    
    if index < len(data) and data[index]['Modified Julian Date'] == target_mjd:
        return data[index]
    elif index > 0:
        previous_row = data[index - 1]
        prev_mjd = previous_row['Modified Julian Date']
        diff_days = target_mjd - prev_mjd

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
    target_mjd = -98765
    result = find_date(data, target_mjd)
    
    if result:
        japanese_month_display = f"閏{result['Japanese month']}" if result['Is leap month'] == '1' else f"{result['Japanese month']}"
        print(f"Common Date: {result['Common year']}-{result['Common month']:02d}-{result['Common day']:02d}")
        print(f"Japanese Date: {result['Era name']}{result['Japanese year']}年{japanese_month_display}月{result['Japanese day']}日")
    else:
        print("Date not found")

if __name__ == "__main__":
    main()