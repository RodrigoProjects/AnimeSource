<template>
  <div class="relative">
    <img
      src="@/assets/bg.png"
      alt=""
      class="w-full h-80 object-cover object-center opacity-30"
    />
    <div class="flex items-center justify-center w-full">
      <div
        class="quote flex flex-col items-center justify-center w-full p-10"
      >
        <p v-if="quote" class="font-black text-yellow-600 text-xl text-center md:text-3xl">
          " {{ quote.quote.replace('"', "'") }} "
        </p>

        <span v-if="quote" class="w-full p-10 text-center font-bold">
          {{ quote.anime }} - {{ quote.character }}
        </span>
        
      </div>
    </div>
  </div>
</template>

<script>
let axios = require('axios')

export default {
    data() {
      return {
        quote : null
      }
    },
    created: function(){
        axios.get("https://animechan.vercel.app/api/random")
          .then(response => {
            this.quote = response.data
        })
          .catch(e => {
              console.log('Erro no get quote '+ e)
              this.quote = {anime:"Naruto", character:"Naruto", quote:"I will be the hokage!" }
          })
    }
};
</script>

<style>

.quote {
  transform: translateY(-100%)
}

</style>