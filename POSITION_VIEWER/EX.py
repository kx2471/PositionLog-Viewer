import csv
import pandas as pd
import folium
from tkinter import Tk, filedialog
import webbrowser
import os

def extract_lat_lon():
    # 사용자 입력을 통한 파일 경로 설정
    root = Tk()
    root.withdraw()  # GUI 창 숨기기
    
    # 다중 파일 선택
    input_file_paths = filedialog.askopenfilenames(
        title="입력 GNSS 파일을 선택하세요",
        filetypes=[("Log files", "*.log"), ("All files", "*.*")]
    )

    output_file_path = os.path.join(os.path.expanduser("~"), "Desktop", "lat_lon_output.csv")

    # 위도와 경도를 저장할 리스트
    lat_lon_list = []

    # 선택한 각 파일에 대해 GNSS 데이터를 포함한 텍스트 파일 읽기
    for input_file_path in input_file_paths:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if "[GNSS]" in line:
                    # 위도와 경도 추출
                    parts = line.split(',')

                    # 위도와 경도 값을 정수형으로 가져옴
                    latitude_raw = int(parts[6])  # 6번째 값 위도
                    longitude_raw = int(parts[5])  # 5번째 값 경도

                    # 변환
                    latitude = latitude_raw / 10000000.0
                    longitude = longitude_raw / 10000000.0
                    # 예외 처리: 위도와 경도가 0이 아닐 때만 리스트에 추가
                    if latitude != 0 and longitude != 0 and (longitude < 39 and longitude > 32) and (latitude < 143 and latitude > 124):
                    	lat_lon_list.append([latitude, longitude])

    # 결과를 CSV 파일로 출력 (헤더 없이 숫자만 저장)
    with open(output_file_path, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        # 데이터 쓰기 (헤더 없이 숫자만 포함)
        writer.writerows(lat_lon_list)

    print(f"위도와 경도가 {output_file_path}에 숫자만 CSV 형식으로 저장되었습니다.")
    return lat_lon_list  # 리스트 반환

def create_map_from_csv(lat_lon_list):
    # 지도 초기화 (경로의 시작점이 중심점이 됨)
    starting_point = [lat_lon_list[0][1], lat_lon_list[0][0]]  # (위도, 경도)
    my_map = folium.Map(location=starting_point, zoom_start=14)

    # 선을 그릴 경도와 위도를 저장할 리스트
    locations = []

    # 경도와 위도를 locations 리스트에 추가
    for loc in lat_lon_list:
        locations.append((loc[1], loc[0]))  # (경도, 위도)

    # PolyLine으로 선 그리기
    folium.PolyLine(locations, color='blue', weight=2.5, opacity=0.8).add_to(my_map)

    # HTML 파일 경로 설정
    output_map_path = os.path.join(os.path.expanduser("~"), "Desktop", "map.html")

    # 지도 저장
    my_map.save(output_map_path)
    print(f"지도가 {output_map_path}에 저장되었습니다.")

    # HTML 파일 자동 실행
    webbrowser.open('file://' + output_map_path)

# 함수 호출
lat_lon_data = extract_lat_lon()  # CSV 파일 생성 및 경로 반환
create_map_from_csv(lat_lon_data)  # HTML 파일 생성
