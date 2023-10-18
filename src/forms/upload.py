from flask_wtf import FlaskForm
from wtforms import SelectField, DateField, FileField, SubmitField
from wtforms.validators import DataRequired, ValidationError

regions = [
    {
        "name" : 'Qoraqalpog`iston Respublikasi',
        "value" : 1
    },
    {
        "name" : 'Andijon viloyati',
        "value" : 2
    },
    {
        "name" : 'Xorazm viloyati',
        "value" : 3
    },
    {
        "name" : 'Farg`ona viloyati',
        "value" : 4
    },
    {
        "name" : 'Toshkent viloyati',
        "value" : 5
    },
    {
        "name" : 'Surxondaryo viloyati',
        "value" : 6
    },
    {
        "name" : 'Sirdaryo viloyati',
        "value" : 7
    },
    {
        "name" : 'Samarqand viloyati',
        "value" : 8
    },
    {
        "name" : 'Namangan viloyati',
        "value" : 9
    },
    {
        "name" : 'Navoiy viloyati',
        "value" : 10
    },
    {
        "name" : 'Qashqadaryo viloyati',
        "value" : 11
    },
    {
        "name" : 'Jizzax viloyati',
        "value" : 12
    },
    {
        "name" : 'Buxoro viloyati',
        "value" : 13
    },
]

indexes = [
    {
        "name" : 'NDVI',
        "value" : 1
    },
    {
        "name" : 'NDMI',
        "value" : 2
    },
]

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'xlsx'}

def allowed_file(filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class UploadForm(FlaskForm):
    region = SelectField('Viloyat', validators=[DataRequired()],choices=[(reg['value'], reg['name']) for reg in regions])
    index = SelectField('Indeks', validators=[DataRequired()] , choices=[(index['value'], index['name']) for index in indexes])
    date = DateField('Kun', validators=[DataRequired()])
    file = FileField('File', validators=[DataRequired(message='File not chosen')])
    # submit = SubmitField("Ko'rish", id='preview-button')

    def validate_file(self, file):
        fileData = self.data['file']
        print(fileData.filename)
        print(allowed_file(fileData.filename))
        
        if not allowed_file(fileData.filename):
            raise ValidationError("File formati noto'g'ri!!!")