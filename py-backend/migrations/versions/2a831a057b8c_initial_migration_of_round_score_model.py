"""Initial migration of round score model

Revision ID: 2a831a057b8c
Revises: 7057d4f40cd6
Create Date: 2026-03-31 07:36:31.816901

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2a831a057b8c'
down_revision = '7057d4f40cd6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('Round_Score',
    sa.Column('round_score_id', sa.Integer(), nullable=False),
    sa.Column('round_id', sa.Integer(), nullable=False),
    sa.Column('gross_score', sa.Integer(), nullable=False),
    sa.Column('net_score', sa.Integer(), nullable=False),
    sa.Column('par', sa.Integer(), server_default='72', nullable=False),
    sa.Column('to_par_value', sa.String(), nullable=False),
    sa.Column('score_out', sa.Integer(), nullable=True),
    sa.Column('par_out', sa.Integer(), nullable=True),
    sa.Column('score_in', sa.Integer(), nullable=True),
    sa.Column('par_in', sa.Integer(), nullable=True),
    sa.Column('expected_score', sa.Float(), nullable=True),
    sa.Column('expected_score_in', sa.Float(), nullable=True),
    sa.Column('expected_score_out', sa.Float(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['round_id'], ['Round.round_id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('round_score_id'),
    sa.UniqueConstraint('round_score_id')
    )
    # ### end Alembic commands ###


def downgrade():
    op.drop_table('Round_Score')
    # ### end Alembic commands ###
