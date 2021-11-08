const index = Vue.createApp({
    data() {
        return {
            usuarios: [{
                id: 1,
                nomeUsuario: 'PresidenteBolinho',
                senha: '123'
            }]
        }
    }
})

index.component('login-form', {
    props: ['nomeUsario', 'senha'],
    emits: {
        // Sem validação
        click: null,

        // Validar evento submit
        submit: ({nomeUsuario, senha}) => {
            if (nomeUsuario && senha)
                return true
            else {
                console.warn('Argumentos inválidos para o evento submit!')
                alert('Campos vazios.')
                return false
            }
        }
    },
    methods: {
        submitForm(nomeUsuario, senha) {
            this.$emit('submit', {nomeUsuario, senha})
        }
    },
    template: `
    <form>
        <label>Usuário</label>
        <input>
        <label>Senha</label>
        <input type="password">
        <input type="submit">
    </form>
    `
})

index.mount('#index')