"""Add DFIQ context to SearchHistory

Revision ID: 710c224732e1
Revises: 5c3ba044dc64
Create Date: 2023-09-25 18:24:34.111079

"""
# This code is auto generated. Ignore linter errors.
# pylint: skip-file

# revision identifiers, used by Alembic.
revision = "710c224732e1"
down_revision = "5c3ba044dc64"

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("searchhistory", schema=None) as batch_op:
        batch_op.add_column(sa.Column("scenario_id", sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column("facet_id", sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column("question_id", sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column("approach_id", sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, "facet", ["facet_id"], ["id"])
        batch_op.create_foreign_key(None, "scenario", ["scenario_id"], ["id"])
        batch_op.create_foreign_key(
            None, "investigativequestionapproach", ["approach_id"], ["id"]
        )
        batch_op.create_foreign_key(
            None, "investigativequestion", ["question_id"], ["id"]
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("searchhistory", schema=None) as batch_op:
        batch_op.drop_constraint(None, type_="foreignkey")
        batch_op.drop_constraint(None, type_="foreignkey")
        batch_op.drop_constraint(None, type_="foreignkey")
        batch_op.drop_constraint(None, type_="foreignkey")
        batch_op.drop_column("approach_id")
        batch_op.drop_column("question_id")
        batch_op.drop_column("facet_id")
        batch_op.drop_column("scenario_id")

    # ### end Alembic commands ###
