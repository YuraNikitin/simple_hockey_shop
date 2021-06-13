<template>
    <div>
      <div class="first-block">
        <TimeTable />
      </div>

      <div class="second-block">
        <News />
      </div>
    </div>
</template>

<script src="./_Calendar.js" lang="js"></script>
<style  lang="scss" scoped>
  .first-block {
    background-color: #fff;
    border: 1px solid #c5dee9;
    padding: 30px 25px;
    margin-bottom: 30px;
  }

  .second-block {
    background-color: #0085d6;
    margin-top: 30px;
  }
</style>
