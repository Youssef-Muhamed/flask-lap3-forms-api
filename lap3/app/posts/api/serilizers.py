from flask_restful import fields
CategorySerilizer= {
    'id': fields.Integer,
    'name': fields.String,
    'desc':     fields.String,
}



postserilizer= {
    'id':fields.Integer,
    'title' :fields.String,
    'body': fields.String,
    'cat_id': fields.Nested(CategorySerilizer)
}