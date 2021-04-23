"""Initial tables

Revision ID: 648ab2576e11
Revises: 
Create Date: 2021-04-05 10:05:51.476018

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2

# revision identifiers, used by Alembic.
revision = '648ab2576e11'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('scooter',
    sa.Column('serialNo', sa.String(), nullable=False),
    sa.Column('modelNo', sa.String(), nullable=True),
    sa.Column('createdDate', sa.DateTime(), nullable=True),
    sa.Column('modifyDate', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('serialNo')
    )
    op.create_table('location',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('parked', sa.Boolean(), nullable=True),
    sa.Column('coordinates', geoalchemy2.types.Geometry(geometry_type='POINT', from_text='ST_GeomFromEWKT', name='geometry'), nullable=True),
    sa.Column('scooterId', sa.String(), nullable=True),
    sa.Column('createdDate', sa.DateTime(), nullable=True),
    sa.Column('modifyDate', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['scooterId'], ['scooter.serialNo'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('location')
    op.drop_table('scooter')
    # ### end Alembic commands ###
