plt.plot(range(1, max_components+1), train_mses, label='train')
plt.plot(range(1, max_components+1), val_mses, label='val')
plt.fill_between(range(1, max_components+1), val_mses-val_stds, val_mses+val_stds, color='r', alpha=0.2, label='+/- 1 std')
plt.yscale('log')
plt.axvline(best_n, ls='--', c='k', label=f'best n = {best_n}')
plt.legend()
xticks = list(range(0, max_components+1, 25)) + [best_n]
xticks[0] = 1
plt.xticks(xticks);
plt.xlabel('n components')
plt.ylabel('MSE')
plt.title("PCR Model\nCross Validation for Choosing N Components");