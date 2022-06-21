import {createStore} from  'vuex'

export default createStore({
    state:{
        access:'',
        refresh: ''
    },
    mutations:{
        initializeStore(state){
            if (localStorage.getItem("access")) {
                state.access = localStorage.getItem("access")
            }else{
                state.access = ''
            }
        },
        actions:{

        },modules:{

        }
    }
})