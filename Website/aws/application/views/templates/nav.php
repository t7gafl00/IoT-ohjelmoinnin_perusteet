<div class="row no-gutters">
  <div class="col-12">

    <ul class="nav nav-tabs bg-dark " id="myTab" role="tablist" style="font-size: 60%">
    <!--<ul class="nav nav-tabs bg-dark " id="myTab" role="tablist" style="font-size: 10px">-->
      <li class="nav-item" style="width: 25%">
        <a class="nav-link <?php if($this->uri->uri_string() == 'Data/temperature') { echo 'active text-black'; } else { echo 'text-light'; } ?>" href="<?php echo site_url('Data/temperature'); ?> ">Temperature</a>
      </li>
      <li class="nav-item" style="width: 25%">
        <a class="nav-link <?php if($this->uri->uri_string() == 'Data/pressure') { echo 'active text-black'; } else { echo 'text-light'; } ?>" href="<?php echo site_url('Data/pressure'); ?>">Pressure</a>
      </li>
      <li class="nav-item" style="width: 25%">
        <a class="nav-link <?php if($this->uri->uri_string() == 'Data/humidity') { echo 'active text-black'; } else { echo 'text-light'; } ?>" href="<?php echo site_url('Data/humidity'); ?>">Humidity</a>
      </li>
      <li class="nav-item" style="width: 25%">
        <a class="nav-link <?php if($this->uri->uri_string() == 'Data/luminance') { echo 'active text-black'; } else { echo 'text-light'; } ?>" href="<?php echo site_url('Data/luminance'); ?>">Luminance</a>
      </li>
    </ul>

  </div>
</div>
