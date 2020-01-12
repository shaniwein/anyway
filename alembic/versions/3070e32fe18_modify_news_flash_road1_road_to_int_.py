"""modify news_flash road1 road to int fields

Revision ID: 3070e32fe18
Revises: 550a47a98675
Create Date: 2019-03-28 14:17:57.748232

"""

# revision identifiers, used by Alembic.
revision = '3070e32fe18'
down_revision = '550a47a98675'
branch_labels = None
depends_on = None

from alembic import op


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.execute('ALTER TABLE news_flash ALTER COLUMN road1 TYPE INT USING road1::integer')
    op.execute('ALTER TABLE news_flash ALTER COLUMN road2 TYPE INT USING road2::integer')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.execute('ALTER TABLE news_flash ALTER COLUMN road2 TYPE DECIMAL USING road2::decimal')
    op.execute('ALTER TABLE news_flash ALTER COLUMN road1 TYPE DECIMAL USING road1::decimal')
    ### end Alembic commands ###
