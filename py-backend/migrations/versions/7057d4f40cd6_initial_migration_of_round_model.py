"""Initial migration of round model

Revision ID: 7057d4f40cd6
Revises: b8cf35efde5b
Create Date: 2026-03-31 06:46:25.990588

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7057d4f40cd6'
down_revision = 'b8cf35efde5b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('Round',
    sa.Column('round_id', sa.Integer(), nullable=False),
    sa.Column('ghin_id', sa.Integer(), nullable=True),
    sa.Column('third_party_id', sa.Integer(), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('third_party_course_id', sa.Integer(), nullable=True),
    sa.Column('tee_id', sa.Integer(), nullable=True),
    sa.Column('ghin_tee_id', sa.Integer(), nullable=True),
    sa.Column('third_party_tee_id', sa.Integer(), nullable=True),
    sa.Column('course_rating_id', sa.Integer(), nullable=False),
    sa.Column('person_id', sa.Integer(), nullable=False),
    sa.Column('ghin_number', sa.String(length=10), nullable=False),
    sa.Column('person_ss_id', sa.String(), nullable=True),
    sa.Column('course_name', sa.String(), nullable=False),
    sa.Column('tee_name', sa.String(), nullable=False),
    sa.Column('round_date', sa.DATE(), server_default=sa.text('now()'), nullable=False),
    sa.Column('count_in_stats', sa.Boolean(), server_default='t', nullable=False),
    sa.Column('count_in_hanicap', sa.Boolean(), server_default='t', nullable=False),
    sa.Column('lock_round', sa.Boolean(), server_default='f', nullable=False),
    sa.Column('holes_played', sa.Integer(), server_default='18', nullable=False),
    sa.Column('start_time', sa.Time(), nullable=True),
    sa.Column('end_time', sa.Time(), nullable=True),
    sa.Column('total_time', sa.Time(), nullable=True),
    sa.Column('transportation', sa.Enum('W', 'C', 'P', 'M', 'O', name='Round_Transportation'), server_default='W', nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['course_id'], ['Course.course_id'], onupdate='CASCADE', ondelete='CASCADE'),
    # sa.ForeignKeyConstraint(['course_name'], ['Course.name'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['course_rating_id'], ['Course_Rating.course_rating_id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['ghin_number'], ['Person.ghin_number'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['person_id'], ['Person.person_id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['tee_id'], ['Tee.tee_id'], onupdate='CASCADE', ondelete='CASCADE'),
    # sa.ForeignKeyConstraint(['tee_name'], ['Tee.name'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('round_id'),
    sa.UniqueConstraint('ghin_id'),
    sa.UniqueConstraint('round_id'),
    sa.UniqueConstraint('third_party_course_id'),
    sa.UniqueConstraint('third_party_id')
    )

def downgrade():
    op.drop_table('Round')
    # ### end Alembic commands ###
