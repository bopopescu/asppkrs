from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Breeds (db.Model):

    id = db.Column(db.Integer, primary_key=True)
    breed  = db.Column(db.String, nullable = False)
    latitude  = db.Column(db.Float, nullable = False)
    longtitude  = db.Column(db.Float, nullable = False)

    selfprice1  = db.Column(db.Float, nullable = False)
    selfprice2  = db.Column(db.Float, nullable = False)
    selfprice3  = db.Column(db.Float, nullable = False)
    selfprice4  = db.Column(db.Float, nullable = False)
    selfprice5  = db.Column(db.Float, nullable = False)

    subsidies1 = db.Column(db.Float, nullable = False)
    subsidies2 = db.Column(db.Float, nullable = False)
    subsidies3 = db.Column(db.Float, nullable = False)
    subsidies4 = db.Column(db.Float, nullable = False)
    subsidies5 = db.Column(db.Float, nullable = False)

    tradeprice1 = db.Column(db.Float, nullable = False)
    tradeprice2 = db.Column(db.Float, nullable = False)
    tradeprice3 = db.Column(db.Float, nullable = False)
    tradeprice4 = db.Column(db.Float, nullable = False)
    tradeprice5 = db.Column(db.Float, nullable = False)

    rent_with_sub1  = db.Column(db.Float, nullable = False)
    rent_with_sub2  = db.Column(db.Float, nullable = False)
    rent_with_sub3  = db.Column(db.Float, nullable = False)
    rent_with_sub4  = db.Column(db.Float, nullable = False)
    rent_with_sub5  = db.Column(db.Float, nullable = False)

    rent_without_sub1  = db.Column(db.Float, nullable = False)
    rent_without_sub2  = db.Column(db.Float, nullable = False)
    rent_without_sub3  = db.Column(db.Float, nullable = False)
    rent_without_sub4  = db.Column(db.Float, nullable = False)
    rent_without_sub5  = db.Column(db.Float, nullable = False)

    lifetime1  = db.Column(db.Float, nullable = False)
    lifetime2  = db.Column(db.Float, nullable = False)
    lifetime3  = db.Column(db.Float, nullable = False)
    lifetime4  = db.Column(db.Float, nullable = False)
    lifetime5  = db.Column(db.Float, nullable = False)

    offspring1  = db.Column(db.Float, nullable = False)
    offspring2  = db.Column(db.Float, nullable = False)
    offspring3  = db.Column(db.Float, nullable = False)
    offspring4  = db.Column(db.Float, nullable = False)
    offspring5  = db.Column(db.Float, nullable = False)

    mortality1 = db.Column(db.Float, nullable = False)
    mortality2 = db.Column(db.Float, nullable = False)
    mortality3 = db.Column(db.Float, nullable = False)
    mortality4 = db.Column(db.Float, nullable = False)
    mortality5 = db.Column(db.Float, nullable = False)

    yeild1 = db.Column(db.Float, nullable = False)
    yeild2 = db.Column(db.Float, nullable = False)
    yeild3 = db.Column(db.Float, nullable = False)
    yeild4 = db.Column(db.Float, nullable = False)
    yeild5 = db.Column(db.Float, nullable = False)

    fat_content1 = db.Column(db.Float, nullable = False)
    fat_content2 = db.Column(db.Float, nullable = False)
    fat_content3 = db.Column(db.Float, nullable = False)
    fat_content4 = db.Column(db.Float, nullable = False)
    fat_content5 = db.Column(db.Float, nullable = False)

    protein_content1 = db.Column(db.Float, nullable = False)
    protein_content2 = db.Column(db.Float, nullable = False)
    protein_content3 = db.Column(db.Float, nullable = False)
    protein_content4 = db.Column(db.Float, nullable = False)
    protein_content5 = db.Column(db.Float, nullable = False)



    def __repr__(self):
        return '<CowsBreeds {} {}>'.format(self.breed, self.yeild)