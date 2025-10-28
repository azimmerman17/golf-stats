"""Initial Migration of the course rating model

Revision ID: 39871f8fd94b
Revises: f6e84044cdd3
Create Date: 2025-10-27 21:40:34.584976

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '39871f8fd94b'
down_revision = 'f6e84044cdd3'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('Course_Rating',
    sa.Column('course_rating_id', sa.Integer(), nullable=False),
    sa.Column('tee_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('hole_count', sa.Integer(), server_default='18', nullable=True),
    sa.Column('gender', sa.Enum('M', 'F', name='course_rating_gender'), server_default='M', nullable=False),
    sa.Column('start_hole', sa.Integer(), server_default='1', nullable=False),
    sa.Column('course_rating', sa.FLOAT(), nullable=False),
    sa.Column('slope', sa.Integer(), nullable=False),
    sa.Column('par', sa.Integer(), nullable=False),
    sa.Column('bogey_rating', sa.FLOAT(), nullable=True),
    sa.Column('effective_date', sa.DATE(), server_default=sa.text('now()'), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['tee_id'], ['Tee.tee_id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('course_rating_id')
    )
    # ### end Alembic commands ###


def downgrade():
    op.drop_table('Course_Rating')
    # ### end Alembic commands ###
