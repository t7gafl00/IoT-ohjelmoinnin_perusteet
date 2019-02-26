<?php
class Data_model extends CI_Model {

  public function __construct()
  {
    $this->load->database();
  }

  public function get_temperature() {
  $this->db->select('date, temperature');
  $this->db->from('iot');
  /*
  $this->db->where('date >= now() - INTERVAL 1 DAY AND date <= now()');
  */

  $this->db->order_by('date', 'asc');
  return $this->db->get()->result_array();
  }

  public function get_pressure() {
  $this->db->select('date, pressure');
  $this->db->from('iot');

  $this->db->order_by('date', 'asc');
  return $this->db->get()->result_array();
  }

  public function get_humidity() {
    $this->db->select('date, humidity');
    $this->db->from('iot');

    $this->db->order_by('date', 'asc');
    return $this->db->get()->result_array();
  }

  public function get_luminance() {
    $this->db->select('date, luminance');
    $this->db->from('iot');

    $this->db->order_by('date', 'asc');
    return $this->db->get()->result_array();
  }
}
