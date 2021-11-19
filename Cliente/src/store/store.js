import { createStore } from 'vuex'

const store = createStore({
    state() {
        return {
            style: {
                modo: 'claro'
            },
            msg: 'Agora, continua funcionando?!!!'
        }
    },
    getters: {
        getMsg(state) {
            return state.msg
        },
        getModo(state) {
            return state.style.modo
        }
    }
})

export default store