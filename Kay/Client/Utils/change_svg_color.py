
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPainter
from PyQt5.QtSvg import QSvgRenderer
from xml.etree import ElementTree


def change_svg_color(path, color):
    tree = ElementTree.parse(path)
    root = tree.getroot()

    # SVG의 네임스페이스 정의
    namespaces = {'ns': 'http://www.w3.org/2000/svg'}

    for element in root.findall(".//ns:path", namespaces):
        element.attrib['fill'] = color  # 직접 'fill' 속성을 설정합니다.

    # 변환된 XML을 문자열로 변환
    xml = ElementTree.tostring(root, encoding='unicode')

    renderer = QSvgRenderer()
    renderer.load(bytearray(xml.encode('utf-8')))

    image = QImage(35, 35, QImage.Format_ARGB32)
    image.fill(Qt.transparent)

    painter = QPainter(image)
    renderer.render(painter)
    painter.end()

    pixmap = QPixmap.fromImage(image)
    return QIcon(pixmap)