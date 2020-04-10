import exifread
import requests


class PhotoExifInfo():
    
    def __init__(self,photo_path):
        self.photo_path = photo_path
        self.baidu_map_ak = "your baidu map key"
        self.image_info_dict={}
        self.tags ={}
        self.interested_keys = [
            'EXIF ExposureMode',\
            'EXIF ExposureTime',\
            'EXIF Flash',\
            'EXIF ISOSpeedRatings',\
            'Image Model',\
            'EXIF ExifImageWidth',\
            'EXIF ExifImageLength',\
            'Image DateTime',\
            'EXIF DateTimeOriginal',\
            'Image Make',\

            # lens
            # jiaoju
        ]
        
        
    def get_tags(self):
        """
        获取照片信息
        """
        image_content = open(self.photo_path, 'rb')
        tags = exifread.process_file(image_content)
        self.tags = tags
        
        for item in self.interested_keys:
            try:
                info = tags[item]
                self.image_info_dict[item] = info
            except:
                print(f'{self.photo_path} has no attribute of {item}')                
                continue
            
        # 遍历获取照片所有信息
        #for j, k in tags.items():
            #print(f"{j} : {k}")
            #print('拍摄时间：', tags['EXIF DateTimeOriginal'])
            #print('照相机制造商：', tags['Image Make'])
            #print('照相机型号：', tags['Image Model'])
            #print('照片尺寸：', tags['EXIF ExifImageWidth'], tags['EXIF ExifImageLength'])
            
     
        image_content.close()
       

    def get_lng_lat(self):
        """经纬度转换"""
        tags = self.tags
        try:
            # 纬度
            LatRef = tags["GPS GPSLatitudeRef"].printable
            Lat = tags["GPS GPSLatitude"].printable[1:-1].replace(" ", "").replace("/", ",").split(",")
            Lat = float(Lat[0]) + float(Lat[1]) / 60 + float(Lat[2]) / 3600
            if LatRef != "N":
                Lat = Lat * (-1)
            # 经度
            LonRef = tags["GPS GPSLongitudeRef"].printable
            Lon = tags["GPS GPSLongitude"].printable[1:-1].replace(" ", "").replace("/", ",").split(",")
            Lon = float(Lon[0]) + float(Lon[1]) / 60 + float(Lon[2]) / 3600
            if LonRef != "E":
                Lon = Lon * (-1)
            return Lat,Lon
        except:
            print('Unable to get')



    def get_city_info(self):
        result = self.get_lng_lat()
        if result:
            Lat, Lon = result
            url = "https://api.map.baidu.com/reverse_geocoding/v3/?ak="+self.baidu_map_ak+"&output=json&coordtype=wgs84ll&location=" + str(Lat) + ',' + str(Lon)
            url = "https://api.map.baidu.com/reverse_geocoding/v3/?ak="+self.baidu_map_ak+"&output=json&coordtype=wgs84ll&location=31.225696563611,121.49884033194"
            response = requests.get(url).json()
            status = response['status']
            if status == 0:
                address = response['result']['formatted_address']
                if address != "":
                    self.image_info_dict['Position'] = address
            else:
                print('baidu_map error')
    
    
    
    def get_image_info(self):
        self.get_tags()
        self.get_city_info()
        return self.image_info_dict
    
    
    
if __name__ == '__main__':
    result = PhotoExifInfo("test.jpeg").get_image_info()
    
    for j, k in result.items():
        print(f"{j} : {k}")



#"""
##!/usr/bin/env python
## coding:utf-8
## @Date    : 2019/3/12 6:48 PM
## @File    : exif.py
## @Author  : sevck (sevck@jdsec.cn)
## @Link    : https://www.javasec.cn
## -------------------------------------------------------------------------  

#import exifread
#import re
#import json
#import requests
#import sys


#def latitude_and_longitude_convert_to_decimal_system(*arg):
    #"""
    #经纬度转为小数, 作者尝试适用于iphone6、ipad2以上的拍照的照片，
    #:param arg:
    #:return: 十进制小数
    #"""
    #return float(arg[0]) + ((float(arg[1]) + (float(arg[2].split('/')[0]) / float(arg[2].split('/')[-1]) / 60)) / 60)


#def find_GPS_image(pic_path):
    #GPS = {}
    #date = ''
    #with open(pic_path, 'rb') as f:
        #tags = exifread.process_file(f)
        #for tag, value in tags.items():
            #if re.match('Image Make', tag):
                #print('[*] 品牌信息: ' + str(value))
            #if re.match('Image Model', tag):
                #print('[*] 具体型号: ' + str(value))
            #if re.match('EXIF LensModel', tag):
                #print('[*] 摄像头信息: ' + str(value))
            #if re.match('GPS GPSLatitudeRef', tag):
                #GPS['GPSLatitudeRef'] = str(value)
            #elif re.match('GPS GPSLongitudeRef', tag):
                #GPS['GPSLongitudeRef'] = str(value)
            #elif re.match('GPS GPSAltitudeRef', tag):
                #GPS['GPSAltitudeRef'] = str(value)
            #elif re.match('GPS GPSLatitude', tag):
                #try:
                    #match_result = re.match('\[(\w*),(\w*),(\w.*)/(\w.*)\]', str(value)).groups()
                    #GPS['GPSLatitude'] = int(match_result[0]), int(match_result[1]), int(match_result[2])
                #except:
                    #deg, min, sec = [x.replace(' ', '') for x in str(value)[1:-1].split(',')]
                    #GPS['GPSLatitude'] = latitude_and_longitude_convert_to_decimal_system(deg, min, sec)
            #elif re.match('GPS GPSLongitude', tag):
                #try:
                    #match_result = re.match('\[(\w*),(\w*),(\w.*)/(\w.*)\]', str(value)).groups()
                    #GPS['GPSLongitude'] = int(match_result[0]), int(match_result[1]), int(match_result[2])
                #except:
                    #deg, min, sec = [x.replace(' ', '') for x in str(value)[1:-1].split(',')]
                    #GPS['GPSLongitude'] = latitude_and_longitude_convert_to_decimal_system(deg, min, sec)
            #elif re.match('GPS GPSAltitude', tag):
                #GPS['GPSAltitude'] = str(value)
            #elif re.match('.*Date.*', tag):
                #date = str(value)
    ##print({'GPS_information':GPS, 'date_information': date})
    #print('[*] 拍摄时间: '+ date)
    #return {'GPS_information': GPS, 'date_information': date}


#def find_address_from_GPS(GPS):
    #"""
    #使用Geocoding API把经纬度坐标转换为结构化地址。
    #:param GPS:
    #:return:
    #"""
    #secret_key = ''
    #if not GPS['GPS_information']:
        #return '该照片无GPS信息'
    #lat, lng = GPS['GPS_information']['GPSLatitude'], GPS['GPS_information']['GPSLongitude']
    #print('[*] 经度: ' + str(lat) + ', 纬度: ' + str(lng))
    #baidu_map_api = "http://api.map.baidu.com/geocoder/v2/?ak={0}&callback=renderReverse&location={1},{2}s&output=json&pois=0".format(
        #secret_key, lat, lng)
    #response = requests.get(baidu_map_api)
    #content = response.text.replace("renderReverse&&renderReverse(", "")[:-1]
    ##print(content)
    #baidu_map_address = json.loads(content)
    #formatted_address = baidu_map_address["result"]["formatted_address"]
    ## province = baidu_map_address["result"]["addressComponent"]["province"]
    ## city = baidu_map_address["result"]["addressComponent"]["city"]
    ## district = baidu_map_address["result"]["addressComponent"]["district"]
    #return formatted_address


#img_path = sys.argv[1]
#if len(img_path) >= 2:
    #print('[*] 打开文件: '+ img_path)
    #GPS_info = find_GPS_image(pic_path=img_path)
    #address = find_address_from_GPS(GPS=GPS_info)
    #print('[*] 位置信息: '+address)
#else:
    #print('python script.py filename')"""
