"""Initial Migration of the facility season model

Revision ID: 35de02397413
Revises: b316e18c2b6c
Create Date: 2025-10-30 04:36:30.266818

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '35de02397413'
down_revision = 'b316e18c2b6c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('Facility_Season',
    sa.Column('facility_season_id', sa.Integer(), nullable=False),
    sa.Column('facility_id', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.String(length=50), nullable=True),
    sa.Column('end_date', sa.String(length=50), nullable=True),
    sa.Column('year_round', sa.Boolean(), server_default='0', nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['facility_id'], ['Facility.facility_id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('facility_season_id'),
    sa.UniqueConstraint('facility_season_id')
    )

    # ### end Alembic commands ###


def downgrade():
    op.drop_table('Facility_Season')
    # ### end Alembic commands ###
