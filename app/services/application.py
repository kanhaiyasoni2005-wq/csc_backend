# from sqlalchemy.orm import Session
# from app.schemas.application import applicationSchema
# from app.models.application import Application
# def create_service(data:applicationSchema,db:Session):
#     new_service = Application(
#                 application_name = data.application_name,
#                 user_name = data.user_name,
#                 user_no = data.user_no,
#                 application_price = data.application_price,
#                 document = data.document,
#                 image = data.image
#     )
#     db.add(new_service)
#     db.commit()
#     db.refresh(new_service)
#     return new_service

# def fatch_application(db:Session):
#     data = db.query(Application).all()
#     return data