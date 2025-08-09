lasso_pcr = make_pipeline(StandardScaler(),
                    PolynomialFeatures(d, include_bias=False),
                    PCA(),
                    LassoCV(alphas=np.logspace(-4,0), eps=0.0001))