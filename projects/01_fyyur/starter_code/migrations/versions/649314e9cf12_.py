"""empty message

Revision ID: 649314e9cf12
Revises: 
Create Date: 2021-11-10 16:59:14.570714

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '649314e9cf12'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('website_link', sa.String(), nullable=True))
    op.add_column('Artist', sa.Column('isLooking', sa.Boolean(), nullable=True))
    op.add_column('Artist', sa.Column('description', sa.String(), nullable=True))
    op.add_column('Venue', sa.Column('genre', sa.String(), nullable=True))
    op.add_column('Venue', sa.Column('website_link', sa.String(), nullable=True))
    op.add_column('Venue', sa.Column('isTalent', sa.Boolean(), nullable=True))
    op.add_column('Venue', sa.Column('description', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'description')
    op.drop_column('Venue', 'isTalent')
    op.drop_column('Venue', 'website_link')
    op.drop_column('Venue', 'genre')
    op.drop_column('Artist', 'description')
    op.drop_column('Artist', 'isLooking')
    op.drop_column('Artist', 'website_link')
    # ### end Alembic commands ###
