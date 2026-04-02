"""Initial migration of round hole model

Revision ID: 34ceea68643d
Revises: 2a831a057b8c
Create Date: 2026-04-02 05:49:35.516811

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '34ceea68643d'
down_revision = '2a831a057b8c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('Round_Handicap',
    sa.Column('round_handicap_id', sa.Integer(), nullable=False),
    sa.Column('round_id', sa.Integer(), nullable=False),
    sa.Column('gross_score', sa.Integer(), nullable=False),
    sa.Column('esc_score', sa.Integer(), nullable=False),
    sa.Column('holes_played', sa.Integer(), nullable=False),
    sa.Column('differential', sa.Float(), nullable=True),
    sa.Column('course_rating', sa.Float(), nullable=True),
    sa.Column('slope_rating', sa.Integer(), nullable=True),
    sa.Column('course_handicap', sa.Integer(), nullable=True),
    sa.Column('pcc', sa.Float(), nullable=True),
    sa.Column('exceptional', sa.Boolean(), server_default='f', nullable=False),
    sa.Column('net_differential', sa.Float(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['round_id'], ['Round.round_id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('round_handicap_id'),
    sa.UniqueConstraint('round_handicap_id')
    )
    op.create_table('Round_Hole',
    sa.Column('round_hole_id', sa.Integer(), nullable=False),
    sa.Column('round_id', sa.Integer(), nullable=False),
    sa.Column('hole_id', sa.Integer(), nullable=False),
    sa.Column('ghin_hole_id', sa.Integer(), nullable=True),
    sa.Column('third_party_hole_id', sa.Integer(), nullable=True),
    sa.Column('third_party_round_hole_id', sa.Integer(), nullable=True),
    sa.Column('hole_number', sa.Integer(), nullable=False),
    sa.Column('yardage', sa.Integer(), nullable=False),
    sa.Column('par', sa.Integer(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('score_vs_par', sa.String(), nullable=True),
    sa.Column('expected_score', sa.Float(), nullable=True),
    sa.Column('esc_score', sa.Integer(), nullable=True),
    sa.Column('stroke_index', sa.Integer(), nullable=True),
    sa.Column('x_hole', sa.Boolean(), server_default='f', nullable=False),
    sa.Column('hole_catagory', sa.Enum('T3', 'S3', 'M3', 'L3', 'T4', 'S4', 'M4', 'L4', 'T5', 'S5', 'M5', 'L5', name='Round_Hole_Catagory'), nullable=True),
    sa.Column('tiger_five_errors', sa.ARRAY(sa.Enum('A', 'B', 'C', 'D', 'E', name='Hole_Tiger_Five')), nullable=True),
    sa.Column('net_tiger_five_errors', sa.ARRAY(sa.Enum('A', 'G', 'H', 'I', 'J', name='Hole_Net_Tiger_Five')), nullable=True),
    sa.Column('fairway_hit', sa.Boolean(), server_default='f', nullable=False),
    sa.Column('drive_miss', sa.Enum('NW', 'N', 'NE', 'W', 'E', 'SW', 'S', 'SE', 'OW', 'OEON', 'OS', name='Round_Hole_Drive_Miss'), nullable=True),
    sa.Column('drive_lie', sa.Enum('F', 'R', 'S', 'X', 'G', 'P', 'H', 'FC', 'W', 'FR', name='Round_Hole_Drive_Lie'), server_default='F', nullable=False),
    sa.Column('approach_distance', sa.Integer(), nullable=True),
    sa.Column('approach_lie', sa.Enum('T', 'F', 'R', 'S', 'X', 'G', 'P', 'H', 'FC', 'W', 'FR', name='Round_Hole_Approach_Lie'), server_default='F', nullable=False),
    sa.Column('prox_to_hole', sa.Integer(), nullable=True),
    sa.Column('prox_to_hole_lie', sa.Enum('F', 'R', 'S', 'X', 'G', 'P', 'H', 'FC', 'W', 'FR', name='Round_Hole_Prox_To_Hole_Lie'), server_default='F', nullable=False),
    sa.Column('green_hit', sa.Boolean(), server_default='f', nullable=False),
    sa.Column('green_miss', sa.Enum('NW', 'N', 'NE', 'W', 'E', 'SW', 'S', 'SE', 'OW', 'OEON', 'OS', name='Round_Hole_Green_Miss'), nullable=True),
    sa.Column('green_hit_plus_one', sa.Boolean(), server_default='f', nullable=False),
    sa.Column('green_miss_lie', sa.Enum('F', 'R', 'S', 'X', 'G', 'P', 'H', 'FC', 'W', 'FR', name='Round_Hole_Green_Miss_Lie'), server_default='F', nullable=False),
    sa.Column('putts', sa.Integer(), nullable=True),
    sa.Column('tee_lat', sa.Float(), nullable=True),
    sa.Column('tee_lon', sa.Float(), nullable=True),
    sa.Column('turn_lat', sa.Float(), nullable=True),
    sa.Column('turn_lon', sa.Float(), nullable=True),
    sa.Column('pin_lat', sa.Float(), nullable=True),
    sa.Column('pin_lon', sa.Float(), nullable=True),
    sa.Column('start_time', sa.Time(), nullable=True),
    sa.Column('end_time', sa.Time(), nullable=True),
    sa.Column('time_per_shot', sa.Interval(), nullable=True),
    sa.Column('sg_total', sa.Float(), nullable=True),
    sa.Column('sg_tee', sa.Float(), nullable=True),
    sa.Column('sg_approach', sa.Float(), nullable=True),
    sa.Column('sg_short_game', sa.Float(), nullable=True),
    sa.Column('sg_putting', sa.Float(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['hole_id'], ['Hole.hole_id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['round_id'], ['Round.round_id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('round_hole_id'),
    sa.UniqueConstraint('round_hole_id')
    )
    # ### end Alembic commands ###

def downgrade():
    op.drop_table('Round_Hole')
    op.drop_table('Round_Handicap')
    # ### end Alembic commands ###
