{
  // Testing ROOT fitter.  Trying to force fit function to satisify f(x_nom)=1
  gROOT->Reset();
  double x_nom = 3.14;
  TF1 * fit_func = new TF1("fit_func", Form("[1]*(x-%f)*(x-%f)+[0]*(x-%f)+1.0", x_nom, x_nom, x_nom), 0.0, 10.);
  // TF1 * fit_func = new TF1("fit_func", Form("[1]*(x-1.5)*(x-1.5)+[0]*(x-1.5)+1.0", x_nom), 0.0, 10.);

  int n_points = 31;
  double x[n_points], y[n_points];
  for (int i=0; i < n_points; i++) {
    x[i] = i*0.1;
    y[i] = sin(x[i]);
  }
  TGraph *gr = new TGraph(n_points, x,y);

  gr->Fit(fit_func);
}
