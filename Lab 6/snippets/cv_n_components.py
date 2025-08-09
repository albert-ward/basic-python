max_components = 200
train_mses = np.empty(max_components)
train_stds = np.empty_like(train_mses)
val_mses = np.empty_like(train_mses)
val_stds = np.empty_like(train_mses)
lm =  LinearRegression()
for i, n in enumerate(range(1, max_components+1)):
    cv = cross_validate(lm,
                        X_pca_train[:,:n+1],
                        y_train,
                        cv=3,
                        scoring='neg_mean_squared_error',
                        return_train_score=True)
    train_mses[i] = -cv['train_score'].mean()
    train_stds[i] = cv['train_score'].std()
    val_mses[i] = -cv['test_score'].mean()
    val_stds[i] = cv['test_score'].std()