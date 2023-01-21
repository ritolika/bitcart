"""Add upload files functionality

Revision ID: 5e08deebdb74
Revises: 12f53bb6513c
Create Date: 2023-01-21 17:59:29.322651

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "5e08deebdb74"
down_revision = "12f53bb6513c"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "files",
        sa.Column("id", sa.Text(), nullable=False),
        sa.Column("filename", sa.Text(), nullable=True),
        sa.Column("user_id", sa.Text(), nullable=True),
        sa.Column("created", sa.DateTime(timezone=True), nullable=False),
        sa.Column("metadata", sa.JSON(), nullable=True),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], name=op.f("files_user_id_users_fkey"), ondelete="SET NULL"),
        sa.PrimaryKeyConstraint("id", name=op.f("files_pkey")),
    )
    op.create_index(op.f("files_id_idx"), "files", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("files_id_idx"), table_name="files")
    op.drop_table("files")
    # ### end Alembic commands ###
