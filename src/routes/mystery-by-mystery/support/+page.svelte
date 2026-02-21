<script lang="ts">
</script>

<svelte:head>
	<title>Mystery by Mystery Support | Code Pasture</title>
	<meta name="description" content="Get help with Mystery by Mystery, a Catholic Rosary companion app for iOS, macOS, Android, Windows, and Linux." />
</svelte:head>

<div class="page">
	<header class="page-header">
		<a href="/" class="back-link">&larr; Code Pasture</a>
	</header>

	<main class="content">
		<h1>Mystery by Mystery Support</h1>

		<section class="section">
			<h2>Contact Us</h2>
			<p>
				For questions, bug reports, or feature requests, please email us at:
			</p>
			<a href="mailto:mystery-by-mystery@codepasture.com" class="email-link">mystery-by-mystery@codepasture.com</a>
		</section>

		<section class="section">
			<h2>Frequently Asked Questions</h2>

			<div class="faq-item">
				<h3>Which mystery set should I pray today?</h3>
				<p>It depends on which mode you chose during setup. In <strong>Daily Schedule</strong> mode, the app follows the traditional weekly pattern: Joyful (Monday, Saturday), Sorrowful (Tuesday, Friday), Glorious (Wednesday, Sunday), and Luminous (Thursday). In <strong>Continuous Cycle</strong> mode, it moves through the mystery sets in order — each time you finish a Rosary, the next set begins automatically.</p>
			</div>

			<div class="faq-item">
				<h3>Can I pick up where I left off?</h3>
				<p>Yes. Your current Rosary session is saved automatically, including which decade you're on. Close the app and come back later — you'll be right where you left off.</p>
			</div>

			<div class="faq-item">
				<h3>What scripture translations are available?</h3>
				<p>Each mystery includes scripture passages in two translations: the Catholic Public Domain Version (CPDV) and the Douay-Rheims Bible. You can switch between them in Settings.</p>
			</div>

			<div class="faq-item">
				<h3>Does the app require an internet connection?</h3>
				<p>No. All prayers, scripture passages, and app functionality work entirely offline. The app never connects to the internet during normal use.</p>
			</div>

			<div class="faq-item">
				<h3>How do donations work?</h3>
				<p>Mystery by Mystery is completely free with no ads or locked features. Optional candle-themed donations are available if you'd like to support development. These are one-time purchases processed through the App Store or Google Play.</p>
			</div>

			<div class="faq-item">
				<h3>Where is my data stored?</h3>
				<p>All prayer history and settings are stored locally on your device in a SQLite database. No data is sent to Code Pasture servers. Your data stays on your device.</p>
			</div>

			<div class="faq-item">
				<h3>Is it available on my platform?</h3>
				<p>Mystery by Mystery is available on iOS, macOS (App Store), Android (Google Play), and Windows and Linux (direct download from GitHub).</p>
			</div>
		</section>

		<section class="section">
			<p class="footer-links">
				<a href="/mystery-by-mystery/privacy">Privacy Policy</a>
			</p>
		</section>
	</main>
</div>

<style>
	.page {
		min-height: 100vh;
		padding: 2rem;
		max-width: 800px;
		margin: 0 auto;
	}

	.page-header {
		margin-bottom: 3rem;
	}

	.back-link {
		color: var(--color-text-muted);
		font-size: 0.9rem;
	}

	.back-link:hover {
		color: var(--color-accent);
	}

	.content h1 {
		font-size: 2rem;
		font-weight: 600;
		margin-bottom: 2rem;
	}

	.section {
		margin-bottom: 3rem;
	}

	.section h2 {
		font-size: 1.25rem;
		font-weight: 600;
		margin-bottom: 1rem;
		color: var(--color-accent);
	}

	.section p {
		color: var(--color-text-muted);
		line-height: 1.7;
	}

	.email-link {
		display: inline-block;
		margin-top: 0.5rem;
		font-size: 1.1rem;
		font-weight: 500;
	}

	.faq-item {
		margin-bottom: 1.5rem;
		padding: 1.25rem;
		background: var(--color-bg-elevated);
		border: 1px solid var(--color-border);
		border-radius: var(--radius-md);
	}

	.faq-item h3 {
		font-size: 1rem;
		font-weight: 600;
		margin-bottom: 0.5rem;
	}

	.faq-item p {
		margin: 0;
		font-size: 0.95rem;
	}

	.footer-links {
		padding-top: 2rem;
		border-top: 1px solid var(--color-border);
	}

	@media (max-width: 768px) {
		.page {
			padding: 1.5rem;
		}

		.content h1 {
			font-size: 1.5rem;
		}
	}
</style>
