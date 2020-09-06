# images2pdf

---

[images2pdf](github.com/hiddenbeginner/images2pdf)는 이미지(사진)들이 들어있는 폴더를 입력 받아서 하나의 PDF 파일로 병합해주는 프로그램입니다.
이 프로젝트는 파이썬의 패키지 [ReportLab](https://pypi.org/project/reportlab/)과 의존성 패키지만을 사용하여 구현된 토이 프로젝트입니다.
- PDF 문서의 용지 크기는 A4 (210mm x 297mm) 크기입니다.
- 이미지 파일 이름 순서대로 PDF에 삽입됩니다.
- PDF 한 페이지마다 한 장의 이미지가 들어갑니다.
- 이미지의 원래 크기대로 삽입되며, 용지의 크기보다 클 경우 가로와 세로 비율을 유지한채로 최대 크기로 삽입됩니다. 

원하시는 기능이 있으시거나 버그를 발견하시면 `issue`에 남겨주세요. 열심히 공부해서 의견을 적극 반영하도록 하겠습니다.


# Quickstart

---

## Clone (Download the code)
- `git` 명령어를 사용하여 이 레포지토리를 클론하거나

~~~bash
> git clone https://github.com/HiddenBeginner/images2pdf.git
~~~

- `Code` 버튼을 클릭하면 등장하는 `Download ZIP`을 이용하여 코드를 다운로드 받습니다.

## Place your image folder in the directory
- 이미지들이 들어있는 폴더를 코드 폴더 안으로 이동시킵니다. 이 때, 이미지의 이름 순서대로 PDF에 삽입되기 때문에 원하는 순서로 이미지 이름을 설정하는 것을 권장합니다.

## Run
- 터미널에서 코드 폴더로 이동 후 다음 명령어를 입력합니다.

~~~bash
> python run.py --images_path <이미지 폴더 이름> --title <"PDF 파일 이름">
~~~ 

- Example

~~~ bash
> python run.py --images_path images --title ExamplePDF
~~~

# Reference

---

[1] [ReportLab](https://pypi.org/project/reportlab/)<br/>
[2] AllTech. (2019, October). Generate PDF with Python - Reportlab[Video file]. Retrieved from [https://youtu.be/ZDR7-iSuwkQ](https://youtu.be/ZDR7-iSuwkQ)<br/>