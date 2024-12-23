"""fill_with_mock_data

Revision ID: 0002
Revises: 0001
Create Date: 2024-11-09 18:05:40.049736

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0002'
down_revision = '0001'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("""
    INSERT INTO executors 
    (id, tags, rating)
    VALUES
    ('1', '["sunglasses", "cool", "epic"]', 5.0),
    ('2', '["good music taste", "quiet"]', 4.8),
    ('3', '["swears"]', 3.4),
    ('4', '["quiet"]', 4.5),
    ('5', '["bad driving", "swears"]', 2.3);
    """)
    op.execute("""
    INSERT INTO zones 
    (id, coin_coeff, display_name)
    VALUES
    ('1', 1.01, 'A little faster road'),
    ('2', 2.0, 'For rich road'),
    ('3', 1.5, 'Good road'),
    ('4', 1.1, 'Paid road'),
    ('5', 1.66, 'Highway to hell'),
    ('6', 3.0, 'Extra good road');
    """)
    op.execute("""
    INSERT INTO tollroads
    (id, bonus_amount)
    VALUES
    ('1', 1.1),
    ('2', 1.5),
    ('3', 2.0);
    """)
    op.execute("""
    INSERT INTO orders
    (id, user_id, zone_id, base_coin_amount)
    VALUES
    ('1', 1, 5, 100.0),
    ('2', 2, 1, 250.0),
    ('3', 3, 6, 1000.0);
    """)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("""
    DELETE FROM executors;
    """)
    op.execute("""
    DELETE FROM orders;
    """)
    op.execute("""
    DELETE FROM tollroads;
    """)
    op.execute("""
    DELETE FROM zones;
    """)
    # ### end Alembic commands ###
