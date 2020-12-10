from fontTools.ttLib import TTFont
import matplotlib.pyplot as plt
import re
import requests

def font_to_xml():
    new_font = None
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/'
                      '537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    font_url = '//k3.autoimg.cn/g1/M09/D2/CF/ChcCQ1sUz16AbTQfAABj6MxuvgQ78..ttf'
    try:
        r = requests.get('http:' + font_url, headers=headers)
        r.raise_for_status()  # 如果不是200，产生异常requests.HTTPError
        # r.encoding = r.apparent_encoding
        print(font_url.split('/')[-1])

        with open('fonts/' + font_url.split('/')[-1], 'wb') as f:
            f.write(r.content)
        new_font = TTFont(r'./fonts/' + font_url.split('/')[-1])
        new_font.saveXML(r'./fonts/a.xml')
    except:
        print("下载字体失败......")
    # font = TTFont(r'./fonts/ChcCQ1sUz2iATgrtAABj9DiBxVE68..ttf')
    # font.saveXML(r'./fonts/a.xml')

def plot_font():
    str = """
<contour>
        <pt x="693" y="-119" on="1"/>
        <pt x="1057" y="-59" on="0"/>
        <pt x="1259" y="26" on="1"/>
        <pt x="1052" y="125" on="0"/>
        <pt x="859" y="213" on="1"/>
        <pt x="962" y="307" on="0"/>
        <pt x="1054" y="433" on="1"/>
        <pt x="722" y="410" on="1"/>
        <pt x="718" y="555" on="1"/>
        <pt x="1134" y="560" on="1"/>
        <pt x="1156" y="634" on="0"/>
        <pt x="1213" y="745" on="1"/>
        <pt x="1300" y="695" on="1"/>
        <pt x="1273" y="1014" on="1"/>
        <pt x="1085" y="785" on="0"/>
        <pt x="793" y="651" on="1"/>
        <pt x="778" y="730" on="0"/>
        <pt x="696" y="791" on="1"/>
        <pt x="984" y="906" on="0"/>
        <pt x="1204" y="1103" on="1"/>
        <pt x="754" y="1095" on="1"/>
        <pt x="766" y="1223" on="1"/>
        <pt x="1308" y="1211" on="1"/>
        <pt x="1276" y="1409" on="1"/>
        <pt x="1072" y="1437" on="0"/>
        <pt x="848" y="1397" on="1"/>
        <pt x="833" y="1484" on="0"/>
        <pt x="815" y="1577" on="1"/>
        <pt x="1375" y="1565" on="0"/>
        <pt x="1847" y="1587" on="1"/>
        <pt x="1874" y="1469" on="1"/>
        <pt x="1665" y="1448" on="0"/>
        <pt x="1430" y="1443" on="1"/>
        <pt x="1415" y="1225" on="1"/>
        <pt x="1974" y="1227" on="1"/>
        <pt x="1975" y="1115" on="1"/>
        <pt x="1513" y="1115" on="1"/>
        <pt x="1736" y="884" on="0"/>
        <pt x="2009" y="804" on="1"/>
        <pt x="1934" y="718" on="0"/>
        <pt x="1900" y="647" on="1"/>
        <pt x="1624" y="768" on="0"/>
        <pt x="1430" y="1042" on="1"/>
        <pt x="1432" y="689" on="1"/>
        <pt x="1314" y="697" on="1"/>
        <pt x="1355" y="657" on="1"/>
        <pt x="1304" y="621" on="0"/>
        <pt x="1279" y="571" on="1"/>
        <pt x="2021" y="547" on="1"/>
        <pt x="2020" y="410" on="1"/>
        <pt x="1748" y="439" on="1"/>
        <pt x="1665" y="217" on="0"/>
        <pt x="1534" y="76" on="1"/>
        <pt x="1768" y="-23" on="0"/>
        <pt x="2003" y="-121" on="1"/>
        <pt x="1919" y="-267" on="1"/>
        <pt x="1670" y="-147" on="0"/>
        <pt x="1416" y="-50" on="1"/>
        <pt x="1194" y="-199" on="0"/>
        <pt x="770" y="-267" on="1"/>
        <pt x="708" y="-191" on="0"/>
      </contour>
      <contour>
        <pt x="19" y="810" on="1"/>
        <pt x="336" y="821" on="1"/>
        <pt x="346" y="1248" on="1"/>
        <pt x="236" y="1267" on="1"/>
        <pt x="227" y="1111" on="0"/>
        <pt x="161" y="979" on="1"/>
        <pt x="66" y="1033" on="0"/>
        <pt x="29" y="1058" on="1"/>
        <pt x="145" y="1342" on="0"/>
        <pt x="224" y="1712" on="1"/>
        <pt x="366" y="1684" on="1"/>
        <pt x="340" y="1548" on="0"/>
        <pt x="300" y="1383" on="1"/>
        <pt x="719" y="1397" on="1"/>
        <pt x="688" y="1256" on="1"/>
        <pt x="497" y="1252" on="1"/>
        <pt x="473" y="844" on="1"/>
        <pt x="480" y="806" on="1"/>
        <pt x="711" y="836" on="1"/>
        <pt x="692" y="693" on="1"/>
        <pt x="496" y="691" on="1"/>
        <pt x="470" y="546" on="0"/>
        <pt x="451" y="452" on="1"/>
        <pt x="666" y="230" on="0"/>
        <pt x="772" y="91" on="1"/>
        <pt x="649" y="-1" on="1"/>
        <pt x="571" y="160" on="0"/>
        <pt x="436" y="285" on="1"/>
        <pt x="387" y="20" on="0"/>
        <pt x="132" y="-262" on="1"/>
        <pt x="92" y="-199" on="0"/>
        <pt x="36" y="-156" on="1"/>
        <pt x="323" y="196" on="0"/>
        <pt x="350" y="670" on="1"/>
        <pt x="50" y="679" on="1"/>
      </contour>
      <contour>
        <pt x="1065" y="260" on="1"/>
        <pt x="1238" y="167" on="0"/>
        <pt x="1386" y="112" on="1"/>
        <pt x="1515" y="237" on="0"/>
        <pt x="1577" y="445" on="1"/>
        <pt x="1196" y="430" on="1"/>
        <pt x="1163" y="325" on="0"/>
      </contour>
      """
    x = [int(i) for i in re.findall(r'<pt x="(.*?)" y=', str)]

    y = [int(i) for i in re.findall(r'y="(.*?)" on=', str)]

    plt.plot(x, y)

    plt.show()


if __name__ == '__main__':
    font_to_xml()
    # plot_font()
