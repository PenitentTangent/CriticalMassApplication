﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Manager : MonoBehaviour {

	public void LoadScene(string scene) {
		SceneManager.LoadScene (scene);
	}

	public void QuitGame() {
		Application.Quit ();
	}
}
