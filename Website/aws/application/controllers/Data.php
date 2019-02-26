<?php
class Data extends CI_Controller {

  public function __construct()
  {
    parent::__construct();
    $this->load->model('data_model');
  }

  public function index()
  {
    $this->temperature();
  }

  public function temperature()
  {
    $data['title'] = "Today\'s temperature measurements";
    $data['unit'] = 'Temperature (°C)';
    $data['min'] = 0;
    $data['max'] = 30;
    $data['values'] = $this->data_model->get_data();
    $data['sensor'] = 'temperature';

    $this->load->view('templates/header');
    $this->load->view('templates/nav');

    $this->load->view('sensors/graph_aws', $data);
    //$this->load->view('sensors/test', $data);
  }

  public function pressure()
  {
    $data['title'] = "Today\'s pressure measurements";
    $data['unit'] = 'Pressure (hPa)';
    $data['min'] = 200;
    $data['max'] = 1100;
    $data['values'] = $this->data_model->get_data();
    $data['sensor'] = 'pressure';

    $this->load->view('templates/header');
    $this->load->view('templates/nav');

    $this->load->view('sensors/graph_aws', $data);
  }

  public function humidity()
  {
    $data['title'] = "Today\'s humidity measurements";
    $data['unit'] = 'Humidity (%)';
    $data['min'] = 0;
    $data['max'] = 100;
    $data['values'] = $this->data_model->get_data();
    $data['sensor'] = 'humidity';

    $this->load->view('templates/header');
    $this->load->view('templates/nav');

    $this->load->view('sensors/graph_aws', $data);
  }

  public function luminance()
  {
    $data['title'] = "Today\'s luminance measurements";
    $data['unit'] = 'Luminance (lux)';
    $data['min'] = 0;
    $data['max'] = 3000;
    $data['values'] = $this->data_model->get_data();
    $data['sensor'] = 'luminance';

    $this->load->view('templates/header');
    $this->load->view('templates/nav');

    $this->load->view('sensors/graph_aws', $data);
  }
}
