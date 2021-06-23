<template>
  <section class="relative block h-64">
    <div
      class="absolute top-0 w-full h-64 bg-center bg-cover"
      :style="{
        'background-image':
          'url(' +
          photo +
          '?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=crop&amp;w=1710&amp;q=40)',
        opacity: '80%',
      }"
    >
      <br /><br />
      <div class="font-bold text-8xl mb-2 text-yellow-100 text-center">
        {{ tipe }}
      </div>
    </div>
    <div
      class="top-auto bottom-0 left-0 right-0 w-full absolute pointer-events-none overflow-hidden"
      style="height: 70px;"
    >
      <svg
        class="absolute bottom-0 overflow-hidden"
        xmlns="http://www.w3.org/2000/svg"
        preserveAspectRatio="none"
        version="1.1"
        viewBox="0 0 2560 100"
        x="0"
        y="0"
      >
        <polygon
          class="text-white fill-current"
          points="2560 0 2560 100 0 100"
        ></polygon>
      </svg>
    </div>
  </section>
</template>

<script>
export default {
  props: {
    photo: String,
    tipe: String,
  },
};
</script>
