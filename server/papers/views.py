from flask import Blueprint
from flask_jwt import current_identity, jwt_required

blueprint = Blueprint('papers', __name__)


@blueprint.route('/api/papers/<username>', methods=['GET'])
def get_papers():
    user = User.query.filter(username=username)
    papers = user.papers.all()
    return papers

@blueprint.route('/api/papers', methods=['POST'])
@jwt_required()
def upload_paper():
    # TODO 文献上传模块，首先将接收到的文献存储到临时文件夹，通过获取文献的DOI号对文献进行重命名，相应与用户关联信息存到数据库
    pass

@blueprint.route('/api/papers/<:id>', methods=['GET'])
@jwt_required()
def get_article():
    paper = Paper.query.find_or_404(id)
    if paper:
        # TODO 如果文献存在，就通过数据库的信息获取到文献的HTML文件
