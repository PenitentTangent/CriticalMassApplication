﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class playMusic : MonoBehaviour, IInteractable {

	public AudioClip music;
	private AudioSource source;

	// Use this for initialization
	void Start () {
		source = gameObject.GetComponent<AudioSource> ();
	}
	
	// Update is called once per frame
	void Update () {
		
	}

	public void Interact(){

		//source.clip = music;
		source.Play();
	}
}
