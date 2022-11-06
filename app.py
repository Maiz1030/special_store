import streamlit as st
import requests
def getAllBookstore():
    url = 'https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M'
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    res = response.json()
    return res
def app():
    st.header('特色書店地圖')
    allBookstore = getAllBookstore()
    st.metric('Total bookstore', len(allBookstore))
    county = st.selectbox('請選擇縣市', ['A', 'B', 'C'])
    district = st.multiselect('請選擇區域', ['a', 'b', 'c', 'd'])
def getSpecificBookstore(items, county, districts):
    specificBookstoreList = []
    for item in items:
        name = item['cityName']
        if county not in name: continue
        for district in districts:
            if district not in name: continue
            specificBookstoreList.append(item)
    return specificBookstoreList
if __name__ == '__main__':
    app()
def getCountyOption(items):
    optionList = []
    for item in items:
            name = item['cutyName'][0:3]# '台北市 中山區'

        if name in optionList:
            continue
        else:
            optionList.append(name)
    return optionList
def getBookstoreInfo(items):
    expanderList = []
    for item in items:
        expander = st.expander(item['name'])
        expander.image(item['representImage'])
        expander.metric('hitRate', item['hitRate'])
        expander.subheader('Introduction')
        expander.write(item['intro'])
        expander.subheader('Address')
        expander.write(item['address'])
        expander.subheader('Open Time')
        expander.write(item['openTime'])
        expander.subheader('Email')
        expander.write(item['email'])
        expanderList.append(expander)
    return expanderList

def app():
    bookstoreList = getAllBookstore()
    countyOption = getCountyOption(bookstoreList)
    st.header('特色書店地圖')
    st.metric('Total bookstore', len(bookstoreList))
    county = st.selectbox('請選擇縣市', countyOption)
    districtOption = getDistrictOption(bookstoreList, county)
    district = st.multiselect('請選擇區域', districtOption)

    specificBookstore = getSpecificBookstore(bookstoreList, county, district)
    num = len(specificBookstore)
    st.write(f'總共有{num}項結果', num)
    getBookstoreInfo = getBookstoreInfo()

    if __name__== '__main__':
        app()
