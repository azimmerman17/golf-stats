"""Initial migration of strokes gained model.

Revision ID: b8cf35efde5b
Revises: 9e5ca252a55a
Create Date: 2026-03-23 20:21:14.713630

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b8cf35efde5b'
down_revision = '9e5ca252a55a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('Strokes_Gained',
    sa.Column('strokes_gained_id', sa.Integer(), nullable=False),
    sa.Column('shot_code', sa.String(length=4), nullable=False),
    sa.Column('distance', sa.Integer(), nullable=False),
    sa.Column('lie', sa.Enum('T', 'F', 'R', 'B', 'X', 'P', 'H', 'G', 'S', name='Strokes_Gained_Lie'), server_default='T', nullable=False),
    sa.Column('pga_tour_value', sa.FLOAT(), nullable=False),
    sa.Column('scratch_value', sa.FLOAT(), nullable=False),
    sa.Column('per_shot_adjust', sa.FLOAT(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('strokes_gained_id'),
    sa.UniqueConstraint('shot_code')
    )

def downgrade():
    op.drop_table('Strokes_Gained')

