<template>
    <div class="main">
      <div class="column-container">
        <div class="left-column">
          <Calendar />
        </div>
        <div class="right-column">
          <div class="person-table">
            <PersonTable />
          </div>

          <div class="standings">
            <Standings />
          </div>

          <div class="stan">

          </div>

          <div class="stan">

          </div>
        </div>
      </div>
    </div>
</template>

<script src="./_Main.js" lang="js"></script>
<style lang="scss" scoped>
.main {
  display: flex;
  justify-content: center;
  background: #e4f4ff;

  .column-container {
    display: flex;
    width: 1200px;

    .left-column {
      min-width: 70%;
      padding-top: 30px;
      padding-bottom: 30px;
    }

    .right-column {
      width: 100%;
      padding-top: 30px;

    }
      .person-table {
        background-color: #fff;
        border: 1px solid #c5dee9;
        padding: 30px 25px 20px;
        margin-bottom: 20px;
        margin-left: 20px;
      }

      .standings {
        background-color: #fff;
        border: 1px solid #c5dee9;
        padding: 15px 0;
        margin-left: 20px;
        margin-bottom: 20px;
      }
  }
}
</style>
