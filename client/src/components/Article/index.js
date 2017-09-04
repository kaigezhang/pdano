import ArticleMeta from './ArticleMeta'
import CommentContainer from './CommentContainer'
import React from 'react'
import agent from 'agent'
import { connect } from 'react-redux'
import marked from 'marked'
import {
    ARTICLE_PAGE_LOADED,
    ARTICLE_PAGE_UNLOADED
} from "../../constants/actionTypes"

const mapStateToProps = state => ({
    ...state.article,
    currentUser: state.common.currentUser
})

const mapDispatchToProps = dispatch => ({
    onLoad: payload => dispatch({
        type: ARTICLE_PAGE_LOADED,
        payload
    }),
    onUnload: () => {
        dispatch({
            type: ARTICLE_PAGE_UNLOADED
        })
    }
})

class Article extends React.Component {
    render () {

    }
}