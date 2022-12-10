<template>
    <nav class="navbar navbar-expand-lg bg-light">
        <div class="container">
            <div class="collapse navbar-collapse" id="navbarText">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                    </li>

                    <li class="nav-item">
                        <router-link class="nav-link "  to="/">Главная</router-link>
                    </li>

                    <li class="nav-item">
                        <router-link class="nav-link "  to="/app/">Создать заявку</router-link>
                    </li>

                    <li class="nav-item">
                        <router-link class="nav-link "  to="/applications/">Заявки</router-link>
                    </li>
                </ul>
                <span class="navbar-text">
                </span>
            </div>
        </div>
    </nav>

</template>
<script>
export default{
    name:'header-nav'
}
</script>
Footer
