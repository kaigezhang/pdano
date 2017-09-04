import { Link } from 'react-router'
import React from 'react'
import agent from '../../agent'
import { connect } from 'react-redux'
import { DELETE_ARTICLE} from "../../constants/actionTypes"

const mapDispatchToProps = dispatch => {
    onClickDelete: payload => dispatch({
        type: DELETE_ARTICLE,
        payload
    })
}

const ArticleActions = props => {
    const article = props.article

    const del = () => {
        props.onClickDelete(agent.Article.del(article.slug))
    }
    if (props.canModify) {
        return (
            <span>
                <Link
                    to={`/edtor/${article.slug}`}
                    className="btn btn-outline btn-secondary btn-sm"
                >
                    <i className="ion-edit"></i>
                </Link>

                <button className="btn btn-outline btn-danger btn-sm" onClick={del}>
                    <i className="ion-trash-a"></i>
                </button>
            </span>
        )
    }

    return (
        <span></span>
    )
}

export default connect(null , mapDispatchToProps)(ArticleActions)