<script lang="ts">
</script>

<section class="hero">
	<div class="hero-content">
		<div class="terminal-line">
			<span class="prompt">$</span> build --from scratch --deploy production
		</div>
		<h1>Full-Stack Development</h1>
		<img src="/code-pasture-logo-transparent.png" alt="0 to 1" class="hero-logo" />
		<p class="tagline">Custom mobile apps and microservices, cultivated with 30 years of experience. From first commit to production.</p>
		<div class="hero-actions">
			<a href="#contact" class="btn-primary">Start a Project</a>
			<a href="https://nathanfox.net" class="btn-secondary" target="_blank" rel="noopener">Read the Blog</a>
		</div>
	</div>
</section>

<style>
	.hero {
		padding: 10rem 2rem 6rem;
		max-width: var(--max-width);
		margin: 0 auto;
	}

	.terminal-line {
		font-family: var(--font-mono);
		font-size: 0.9rem;
		color: var(--color-text-muted);
		margin-bottom: 1.5rem;
		padding: 0.75rem 1rem;
		background: var(--color-bg-elevated);
		border-radius: var(--radius-md);
		border: 1px solid var(--color-border);
		display: inline-block;
	}

	.prompt {
		color: var(--color-accent);
		margin-right: 0.5rem;
	}

	h1 {
		font-size: 3.5rem;
		font-weight: 700;
		line-height: 1.1;
		margin-bottom: 1.5rem;
		letter-spacing: -0.03em;
	}

	.hero-logo {
		height: 100px;
		width: auto;
		margin-bottom: 1.5rem;
	}

	.tagline {
		font-size: 1.2rem;
		color: var(--color-text-muted);
		margin-bottom: 2.5rem;
		max-width: 550px;
		line-height: 1.7;
	}

	.hero-actions {
		display: flex;
		gap: 1rem;
	}

	.btn-primary {
		display: inline-block;
		background: var(--color-accent);
		color: var(--color-bg);
		padding: 0.875rem 1.5rem;
		border-radius: var(--radius-md);
		text-decoration: none;
		font-weight: 600;
		font-size: 0.9rem;
		transition: background var(--transition-fast);
	}

	.btn-primary:hover {
		background: var(--color-accent-hover);
	}

	.btn-secondary {
		display: inline-block;
		background: transparent;
		color: var(--color-text);
		padding: 0.875rem 1.5rem;
		border-radius: var(--radius-md);
		text-decoration: none;
		font-weight: 500;
		font-size: 0.9rem;
		border: 1px solid var(--color-border);
		transition: border-color var(--transition-fast), background var(--transition-fast);
	}

	.btn-secondary:hover {
		border-color: var(--color-text-muted);
		background: var(--color-bg-elevated);
	}

	@media (max-width: 768px) {
		.hero {
			padding: 8rem 1.5rem 4rem;
		}

		h1 {
			font-size: 2.25rem;
		}

		.zero-to-one {
			font-size: 3rem;
		}

		.hero-actions {
			flex-direction: column;
		}
	}
</style>
