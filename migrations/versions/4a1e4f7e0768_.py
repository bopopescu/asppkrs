"""empty message

Revision ID: 4a1e4f7e0768
Revises: 
Create Date: 2019-12-30 13:20:11.375506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a1e4f7e0768'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cows_breeds',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('breed', sa.String(), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=False),
    sa.Column('longtitude', sa.Float(), nullable=False),
    sa.Column('selfprice1', sa.Float(), nullable=False),
    sa.Column('selfprice2', sa.Float(), nullable=False),
    sa.Column('selfprice3', sa.Float(), nullable=False),
    sa.Column('selfprice4', sa.Float(), nullable=False),
    sa.Column('selfprice5', sa.Float(), nullable=False),
    sa.Column('subsidies1', sa.Float(), nullable=False),
    sa.Column('subsidies2', sa.Float(), nullable=False),
    sa.Column('subsidies3', sa.Float(), nullable=False),
    sa.Column('subsidies4', sa.Float(), nullable=False),
    sa.Column('subsidies5', sa.Float(), nullable=False),
    sa.Column('tradeprice1', sa.Float(), nullable=False),
    sa.Column('tradeprice2', sa.Float(), nullable=False),
    sa.Column('tradeprice3', sa.Float(), nullable=False),
    sa.Column('tradeprice4', sa.Float(), nullable=False),
    sa.Column('tradeprice5', sa.Float(), nullable=False),
    sa.Column('rent_with_sub1', sa.Float(), nullable=False),
    sa.Column('rent_with_sub2', sa.Float(), nullable=False),
    sa.Column('rent_with_sub3', sa.Float(), nullable=False),
    sa.Column('rent_with_sub4', sa.Float(), nullable=False),
    sa.Column('rent_with_sub5', sa.Float(), nullable=False),
    sa.Column('rent_without_sub1', sa.Float(), nullable=False),
    sa.Column('rent_without_sub2', sa.Float(), nullable=False),
    sa.Column('rent_without_sub3', sa.Float(), nullable=False),
    sa.Column('rent_without_sub4', sa.Float(), nullable=False),
    sa.Column('rent_without_sub5', sa.Float(), nullable=False),
    sa.Column('lifetime1', sa.Float(), nullable=False),
    sa.Column('lifetime2', sa.Float(), nullable=False),
    sa.Column('lifetime3', sa.Float(), nullable=False),
    sa.Column('lifetime4', sa.Float(), nullable=False),
    sa.Column('lifetime5', sa.Float(), nullable=False),
    sa.Column('offspring1', sa.Float(), nullable=False),
    sa.Column('offspring2', sa.Float(), nullable=False),
    sa.Column('offspring3', sa.Float(), nullable=False),
    sa.Column('offspring4', sa.Float(), nullable=False),
    sa.Column('offspring5', sa.Float(), nullable=False),
    sa.Column('mortality1', sa.Float(), nullable=False),
    sa.Column('mortality2', sa.Float(), nullable=False),
    sa.Column('mortality3', sa.Float(), nullable=False),
    sa.Column('mortality4', sa.Float(), nullable=False),
    sa.Column('mortality5', sa.Float(), nullable=False),
    sa.Column('yeild1', sa.Float(), nullable=False),
    sa.Column('yeild2', sa.Float(), nullable=False),
    sa.Column('yeild3', sa.Float(), nullable=False),
    sa.Column('yeild4', sa.Float(), nullable=False),
    sa.Column('yeild5', sa.Float(), nullable=False),
    sa.Column('fat_content1', sa.Float(), nullable=False),
    sa.Column('fat_content2', sa.Float(), nullable=False),
    sa.Column('fat_content3', sa.Float(), nullable=False),
    sa.Column('fat_content4', sa.Float(), nullable=False),
    sa.Column('fat_content5', sa.Float(), nullable=False),
    sa.Column('protein_content1', sa.Float(), nullable=False),
    sa.Column('protein_content2', sa.Float(), nullable=False),
    sa.Column('protein_content3', sa.Float(), nullable=False),
    sa.Column('protein_content4', sa.Float(), nullable=False),
    sa.Column('protein_content5', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cows_breeds')
    # ### end Alembic commands ###
