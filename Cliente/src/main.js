import { createApp, h } from 'vue'
import routes from './routes'

const SimpleRouterApp = {
    data: () => ({
        rotaAtual: window.location.pathname
    }),
    computed: {
        ViewComponent() {
            const matchingPage = routes[this.rotaAtual] || '404'
            return require(`./paginas/${matchingPage}.vue`).default
        }
    },
    render() {
        return h(this.ViewComponent)
    },
    created() {
        window.addEventListener('popstate', () => {
            this.rotaAtual = window.location.pathname
        })
    }
}

createApp(SimpleRouterApp).mount('#app')
