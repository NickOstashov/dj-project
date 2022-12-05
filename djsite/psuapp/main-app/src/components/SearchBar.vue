<template>
    <div class="search">
        <input type="text" class="search-field" placeholder="Введите поисковый запрос" name = "srh" value = "{{request.GET.search}}" >
        <img src="@/assets/search.svg" alt="" class="search-icon">
    </div>
</template>

<script>

</script>

<style>
.search {
    display: inline-flex;
    background-color: #EEE;
    border-radius: 30px;
    padding: 10px;
    height: 40px;
    margin-right: 20px;
}
  
.search-icon {
    width: 20px;
    height: 20px;
    margin-right: 10px;
    order: -1;
}
  
.search-field {
    width: 300px;
    border: 0; 
    background-color: #EEE;
}
  
.search-field:focus {
    outline: none;
}

@media(max-width:768px) {
    .search{
        display: none;
    }
}

</style>