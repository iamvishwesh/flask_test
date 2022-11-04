from flask import Flask, render_template,request
from pathlib import Path
import PyPDF2
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def rotate():
    if request.method=='POST':
        f=request.files['file']
        a=request.form.get("angle")
        p=request.form.get("page")
        rotatepdf(f.filename,int(a),int(p))
    return render_template('index.html')
def rotatepdf(filename,angle,pageno):
    fileobj=open(filename,'rb') #to open given file
    reader=PyPDF2.PdfFileReader(fileobj) #filereader object
    writer=PyPDF2.PdfFileWriter() #filewriter object
    for pagenum in range(reader.numPages):
        page=reader.getPage(pagenum)
        if (pagenum)==(pageno-1):
            page.rotateClockwise(angle)
        writer.addPage(page)
    convfile=open("rotated.pdf",'wb')
    writer.write(convfile)
    convfile.close()
    return convfile
if __name__ == '__main__':
    app.run(debug=True)
